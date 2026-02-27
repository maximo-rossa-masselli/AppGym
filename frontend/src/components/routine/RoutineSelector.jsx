import { useNavigate } from "react-router-dom";

export default function RoutineSelector({ qrToken, routines }) {
  const navigate = useNavigate();

  function handleSelect(type) {
    navigate(`/public/${qrToken}/routine/${type}`);
  }

  return (
    <div className="space-y-5">
      {routines.map((type) => (
        <button
          key={type}
          onClick={() => handleSelect(type)}
          className="w-full py-4 rounded-2xl text-white font-semibold text-lg shadow-xl transition hover:scale-[1.03] active:scale-95"
          style={{
            background: "rgba(255,255,255,0.15)",
            backdropFilter: "blur(12px)",
          }}
        >
          {formatRoutine(type)}
        </button>
      ))}
    </div>
  );
}

function formatRoutine(type) {
  switch (type) {
    case "upper_body":
      return "UPPER BODY";
    case "lower_body":
      return "LOWER BODY";
    case "full_body":
      return "FULL BODY";
    default:
      return type.toUpperCase();
  }
}
