import axios from "axios";

// Vite usa 'import.meta.env' para acceder a las variables
// Si la variable no existe, cae al localhost por defecto
const API_BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const axiosInstance = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  headers: {
    "Content-Type": "application/json",
  },
});

export default axiosInstance;
