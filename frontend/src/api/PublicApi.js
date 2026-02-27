import axiosInstance from "./axiosInstance";

export async function getPublicGym(qrToken) {
  try {
    const response = await axiosInstance.get(`/public/${qrToken}/`);
    return response.data;
  } catch (error) {
    throw new Error(
      error.response?.data?.detail ||
        "No se pudo obtener la información del gym",
    );
  }
}

export async function getRoutine(qrToken, type) {
  try {
    const response = await axiosInstance.get(
      `/public/${qrToken}/routine/${type}/`,
    );
    return response.data;
  } catch (error) {
    throw new Error(
      error.response?.data?.detail || "No se pudo obtener la rutina",
    );
  }
}
