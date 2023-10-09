# AI-Powered Image Storyteller 📸📖

## Project Overview 🚀

The AI-Powered Image Storyteller is an innovative application that leverages cutting-edge AI models from HuggingFace and OpenAI to turn images into captivating stories. The primary objective is to provide users with a narrative generated from an uploaded image.

### How it Works 🤖

1. **User Uploads an Image:** The user starts by uploading an image of their choice.

2. **Image to Text Conversion:** We employ an HuggingFace model, specifically "salesforce/blip-image-captioning-base," to convert the image into descriptive text.

3. **Langchain Integration:** Using Langchain, we make use of an OpenAI model, specifically GPT-3.5, with a prompt template to craft a compelling story based on the image.

4. **Story to Speech:** The response story is then converted back into spoken words using HuggingFace's speech-to-text model.

5. **User Interface:** The user interacts with the application through a user-friendly interface powered by the Streamlit library.


### Configuration 🛠️

To configure this application, make sure to add an `.env` file for storing the necessary API keys:

```
# .env file
HUGGINGFACE_API_KEY=your_huggingface_api_key
OPENAI_API_KEY=your_openai_api_key
```
### Running the Application 🏃‍♂️

To experience this AI-powered storytelling application, simply run the following command:

```
streamlit run app.py
```
![AI application](./output.png "llm integration")

This project is a testament to the fusion of cutting-edge AI technology with a user-friendly interface, making image-based storytelling accessible and engaging for all.


Happy storytelling! 📸📚🎙️