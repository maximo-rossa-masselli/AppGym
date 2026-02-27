export default function Button({ children, onClick }) {
  return (
    <button
      onClick={onClick}
      className="w-full py-3 rounded-xl bg-black text-white font-medium hover:opacity-90 transition"
    >
      {children}
    </button>
  );
}
