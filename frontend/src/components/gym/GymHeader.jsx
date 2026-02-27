export default function GymHeader({ gym }) {
  return (
    <div className="flex flex-col items-center mb-14 text-center">
      <div className="relative">
        {/* Glow */}
        <div
          className="absolute inset-0 rounded-full blur-3xl opacity-70"
          style={{ backgroundColor: gym.secondary_color }}
        />

        {/* Glass container */}
        <div className="relative bg-white/20 backdrop-blur-xl p-6 rounded-full shadow-2xl border border-white/30">
          <img
            src={gym.logo}
            alt={gym.name}
            className="w-28 h-28 object-contain rounded-full"
          />
        </div>
      </div>

      <h1
        className="mt-8 text-5xl tracking-widest text-white drop-shadow-xl"
        style={{ fontFamily: "var(--font-gym)" }}
      >
        {gym.name}
      </h1>
    </div>
  );
}
