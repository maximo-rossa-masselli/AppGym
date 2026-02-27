import ExerciseItem from "./ExerciseItem";

export default function RoutineCard({ type, exercises }) {
  return (
    <div className="bg-white/90 backdrop-blur-xl rounded-3xl shadow-2xl p-8 border border-white/30">
      <h2
        className="text-3xl tracking-wider text-gray-900 mb-2"
        style={{ fontFamily: "var(--font-gym)" }}
      >
        ENTRENAMIENTO DE HOY
      </h2>

      <p className="text-gray-600 capitalize mb-8">{type.replace("_", " ")}</p>

      <div className="space-y-5">
        {exercises.map((exercise, index) => (
          <ExerciseItem key={index} exercise={exercise} index={index} />
        ))}
      </div>
    </div>
  );
}
