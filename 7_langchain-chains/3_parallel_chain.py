from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

"""
We are building a multi-model AI pipeline that performs three tasks:

1. It takes an input text (in this case, about Support Vector Machines).
2. It runs two tasks in parallel:
   - One model (OpenAI) generates simple notes about the topic.
   - Another model (Hugging Face - Gemma 2B) generates 5 short question-answer pairs.
3. The results from both models are then merged using another OpenAI call,
   producing a single final output that combines the notes and the quiz.

The LangChain `RunnableParallel` utility is used to execute both summarization and quiz generation chains in parallel.
The final chain is visualized using an ASCII graph to show the flow of data across the models and prompts.
"""

# OpenAI model
model1 = ChatOpenAI()

# model2 = ChatAnthropic(model_name="claude-3-7-sonnet-20250219")

# Use HuggingFace's Gemma 2B Instruction-tuned model as an open-source alternative
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")
model2 = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answers from the following text \n {text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=["notes", "quiz"],
)

parser = StrOutputParser()

# -------------------- PARALLEL CHAIN ------------------------

# This chain runs both note generation and quiz generation in parallel
parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,  # Notes: Prompt1 → OpenAI → parse output
        "quiz": prompt2 | model2 | parser,  # Quiz: Prompt2 → HuggingFace → parse output
    }
)

# -------------------- MERGE CHAIN ------------------------

# This takes the output from both branches above and merges them into one final document
merge_chain = prompt3 | model1 | parser  # Merge: Prompt3 → OpenAI → parse output

# -------------------- FINAL CHAIN ------------------------

# The complete pipeline: run both tasks in parallel → merge their outputs
chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({"text": text})

print(result)

chain.get_graph().print_ascii()


# output:

# Support vector machines (SVMs) are used for classification, regression, and outliers detection. They are known for their advantages in high dimensional spaces, memory efficiency, and versatility in kernel functions. However, they also have disadvantages such as over-fitting with too many features, lack of direct probability estimates, and the need for expensive cross-validation.

# Scikit-learn supports both dense and sparse sample vectors for SVMs, with optimal performance using C-ordered numpy.ndarray or scipy.sparse.csr_matrix.

# Here are 5 short question-answer pairs based on the text:

# 1. What are Support Vector Machines (SVMs) used for?
#    - Answer: SVMs are used for classification, regression, and outlier detection.

# 2. What is a key advantage of SVMs?
#    - Answer: Their effectiveness in high-dimensional spaces, even when the number of dimensions is greater than the number of samples.

# 3. What is the role of 'support vectors' in SVMs?
#    - Answer: SVMs use a subset of training points (support vectors) to define the decision function.

# 4. What potential problem can arise when using SVMs with a large number of features?
#    - Answer: Over-fitting, especially if the number of features is significantly larger than the number of samples.

# 5. How can you determine if an SVM is suitable for sparse data?
#    - Answer: The SVM must have been previously fit on the sparse data to make predictions.

# Let me know if you'd like more questions or a different focus!


#             +---------------------------+
#             | Parallel<notes,quiz>Input |
#             +---------------------------+
#                  **               **
#               ***                   ***
#             **                         **
# +----------------+                +----------------+
# | PromptTemplate |                | PromptTemplate |
# +----------------+                +----------------+
#           *                               *
#           *                               *
#           *                               *
#   +------------+                 +-----------------+
#   | ChatOpenAI |                 | ChatHuggingFace |
#   +------------+                 +-----------------+
#           *                               *
#           *                               *
#           *                               *
# +-----------------+              +-----------------+
# | StrOutputParser |              | StrOutputParser |
# +-----------------+              +-----------------+
#                  **               **
#                    ***         ***
#                       **     **
#            +----------------------------+
#            | Parallel<notes,quiz>Output |
#            +----------------------------+
#                           *
#                           *
#                           *
#                  +----------------+
#                  | PromptTemplate |
#                  +----------------+
#                           *
#                           *
#                           *
#                    +------------+
#                    | ChatOpenAI |
#                    +------------+
#                           *
#                           *
#                           *
#                 +-----------------+
#                 | StrOutputParser |
#                 +-----------------+
#                           *
#                           *
#                           *
#               +-----------------------+
#               | StrOutputParserOutput |
#               +-----------------------+
