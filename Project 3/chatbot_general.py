
import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import WikipediaLoader
from langchain.callbacks import get_openai_callback
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import LLMChain
from langchain_community.document_loaders import PyPDFLoader

# Set the API key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# pdf location
folder_path = "pdfs"
# Wikipedia topics
wiki_list = [
    'Colorado_Rockies',
    'List_of_Colorado_Rockies_seasons',
    'Major_League_Baseball_uniforms',
    'History_of_the_Colorado_Rockies',
    'List_of_Major_League_Baseball_awards',
    'Baseball_awards',
    'List of Colorado Rockies team records',
    'List of Colorado Rockies minor league affiliates',
    'List of Colorado Rockies broadcasters',
    '2024_Colorado_Rockies_season',
    '2024_Major_League_Baseball_draft',
    'List_of_Colorado_Rockies_owners_and_executives',
    "Monfort_brothers",
    'List_of_Colorado_Rockies_seasons',
    'Baseball',
    'Baseball_rules',
    'Major_League_Baseball',
    'Origins_of_baseball',
    '2024_Major_League_Baseball_season',
    'List_of_World_Series_champions',
    'Baseball_positioning',
    'Baseball_positions',
    'Batting_(baseball)',
    'Base_running',
    'The_Official_Professional_Baseball_Rules_Book',
    'Inside_baseball_(strategy)',
    'Pitch_(baseball)',
    'Pitcher',
    'Starting_pitcher',
    'Win_probability',
    'Batting_order_(baseball)',
    'Bunt_(baseball)',
    'Double_switch_(baseball)',
    'Lefty-righty_switch',
    'Pickoff',
    'Power_hitter',
    'Power_pitcher',
    'Pull_hitter',
    'Left-handed_specialist#Right-handed_specialist',
    'Small_ball_(baseball)',
    'Intentional_balk',
    'Infield_shift',
    'The_Hidden_Game_of_Baseball',
    'Wins_Above_Replacement'
    ]

def clear_history():
    if 'crc' in st.session_state:
        del st.session_state['crc']

@st.cache_resource
def load_information():
    try:
        documents = []
        for topic in wiki_list:
            wiki_documents = WikipediaLoader(query=topic, load_max_docs=1).load()
            documents.extend(wiki_documents)

        for filename in os.listdir(folder_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(folder_path, filename)
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())

        if not documents:
            st.error("No pdf files or documents found from Wikipedia.")
            return None

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()
        vector_store = Chroma.from_documents(chunks, embedding=embeddings, persist_directory='db')

        llm = ChatOpenAI(model='gpt-4', temperature=0.7)
        retriever = vector_store.as_retriever(search_kwargs={"k": 45})
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )

        custom_template = """
        You are a baseball coach. Answer only questions that pertain to baseball.
        If the human asks questions not related to baseball, remind them that your job is to help
        them learn and answer baseball questions, and ask them for a question on that topic. If they ask a question which
        there is not enough information to answer, tell them you don't know and don't make up an
        answer.

        Current conversation:
        {chat_history}
        Human: {question}
        Context: {context}
        AI Assistant:"""

        CUSTOM_PROMPT = PromptTemplate(
            template=custom_template, input_variables=["chat_history", "question", "context"]
        )

        qa_chain = load_qa_chain(
            llm,
            chain_type="stuff",
            prompt=CUSTOM_PROMPT
        )

        question_generator = LLMChain(llm=llm, prompt=PromptTemplate(
            template="Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.\n\nChat History:\n{chat_history}\n\nFollow Up Input: {question}\n\nStandalone question:",
            input_variables=["chat_history", "question"]
        ))

        crc = ConversationalRetrievalChain(
            retriever=retriever,
            combine_docs_chain=qa_chain,
            question_generator=question_generator,
            return_source_documents=True,
            memory=memory
        )

        return crc
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Begin UI
st.title('Chat with our AI Coach about the Colorado Rockies')

# Load and process Wikipedia content
if 'crc' not in st.session_state:
    st.session_state.crc = load_information()
    if st.session_state.crc:
        st.success("Wikipedia content processed and embedded successfully.")

# Create a form for the question input and submit button
with st.form(key='question_form'):
    question = st.text_input('Input your question')
    submit_button = st.form_submit_button(label='Submit Question')

# Generate response to question
if submit_button and question:
    if 'crc' in st.session_state:
        crc = st.session_state.crc

        with get_openai_callback() as cb:
            result = crc({'question': question})
            response = result['answer']
            source_documents = result['source_documents']

        st.write("Chatbot: " + response)

        # Display chat history
        st.subheader("Chat History")
        messages = crc.memory.chat_memory.messages
        for message in messages:
            if message.type == 'human':
                st.write("User: " + message.content)
            elif message.type == 'ai':
                st.write("AI: " + message.content)
