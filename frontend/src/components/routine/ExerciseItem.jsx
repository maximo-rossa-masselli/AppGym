export default function ExerciseItem({ exercise, index }) {
  const handleWatchVideo = () => {
    // 1. Creamos el término de búsqueda (ej: "Press de Banca ejercicio tutorial shorts")
    const query = encodeURIComponent(
      `${exercise.name} ejercicio técnica shorts`,
    );

    // 2. Construimos la URL de búsqueda.
    // El parámetro 'sp=EgIQAQ%253D%253D' es un filtro de YouTube para mostrar solo Shorts.
    const youtubeUrl = `https://www.youtube.com/results?search_query=${query}&sp=EgIQAQ%253D%253D`;

    // 3. Abrimos en una pestaña nueva para no sacar al usuario de la rutina
    window.open(youtubeUrl, "_blank");
  };

  return (
    <div
      onClick={handleWatchVideo}
      className="flex items-center justify-between p-5 rounded-2xl bg-white shadow-md hover:shadow-xl transition cursor-pointer group active:scale-95"
    >
      <div>
        <div className="flex items-center gap-2">
          <h3 className="font-semibold text-gray-900 text-lg group-hover:text-red-600 transition-colors">
            {exercise.name}
          </h3>
          {/* Pequeño ícono de play para dar feedback visual */}
          <svg
            className="w-4 h-4 text-gray-400 group-hover:text-red-500"
            fill="currentColor"
            viewBox="0 0 24 24"
          >
            <path d="M8 5v14l11-7z" />
          </svg>
        </div>

        <p className="text-gray-500 text-sm mt-1">
          {exercise.sets} sets × {exercise.reps} reps
        </p>
      </div>

      <div className="w-10 h-10 flex items-center justify-center rounded-full bg-black text-white font-bold group-hover:bg-red-600 transition-colors">
        {index + 1}
      </div>
    </div>
  );
}
