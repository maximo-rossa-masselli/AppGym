export default function ExerciseItem({ exercise, index }) {
  return (
    <div className="flex items-center justify-between p-5 rounded-2xl bg-white shadow-md hover:shadow-xl transition">
      <div>
        <h3 className="font-semibold text-gray-900 text-lg">
          {exercise.name}
        </h3>

        <p className="text-gray-500 text-sm mt-1">
          {exercise.sets} sets × {exercise.reps} reps
        </p>
      </div>

      <div className="w-10 h-10 flex items-center justify-center rounded-full bg-black text-white font-bold">
        {index + 1}
      </div>
    </div>
  );
}