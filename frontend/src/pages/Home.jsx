import MobileContainer from "../components/layout/MobileContainer";

export default function Home() {
  return (
    <MobileContainer>
      <div className="flex flex-col items-center justify-center min-h-[80vh] text-center px-6">
        {/* Icono o ilustración simple */}
        <div className="w-24 h-24 bg-black/5 rounded-full flex items-center justify-center mb-8">
          <svg
            className="w-12 h-12 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={1.5}
              d="M12 4v1m6 11h2m-6 0h-2v4m0-11v3m0 0h.01M12 12h4.01M16 20h4M4 12h4m12 0h.01M5 8h2a1 1 0 001-1V5a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1zm12 0h2a1 1 0 001-1V5a1 1 0 00-1-1h-2a1 1 0 00-1 1v2a1 1 0 001 1zM5 20h2a1 1 0 001-1v-2a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1z"
            />
          </svg>
        </div>

        <h1
          className="text-3xl font-bold text-gray-900 mb-4"
          style={{ fontFamily: "var(--font-gym)" }}
        >
          ¡HOLA!
        </h1>

        <p className="text-gray-600 text-lg leading-relaxed">
          Recordá que para acceder a tu rutina debes{" "}
          <span className="font-semibold text-black">escanear el QR</span> de tu
          gimnasio.
        </p>

        <div className="mt-12 p-4 bg-gray-100 rounded-2xl border border-dashed border-gray-300">
          <p className="text-xs text-gray-400 uppercase tracking-widest">
            AppGym Córdoba
          </p>
        </div>
      </div>
    </MobileContainer>
  );
}
