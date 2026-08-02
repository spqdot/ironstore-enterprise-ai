import axios from "axios";

// Backend URL
const API_URL = import.meta.env.VITE_API_URL;

// Send a question to the AI Assistant
export const sendQuestion = async (question) => {
  try {
    const response = await axios.post(`${API_URL}/chat`, {
      question: question,
    });

    return response.data;
  } catch (error) {
    console.error("Error communicating with backend:", error);

    return {
      answer: "Unable to connect to the AI Assistant.",
      sources: [],
    };
  }
};