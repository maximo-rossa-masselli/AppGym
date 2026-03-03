import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "../pages/Home"; // <-- Importar la nueva página
import PublicLanding from "../pages/PublicLanding";
import RoutineView from "../pages/RoutineView";

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Ruta de inicio */}
        <Route path="/" element={<Home />} />

        {/* Rutas existentes */}
        <Route path="/public/:qr_token" element={<PublicLanding />} />
        <Route
          path="/public/:qr_token/routine/:type"
          element={<RoutineView />}
        />

        <Route path="*" element={<div>404 - Not Found</div>} />
      </Routes>
    </BrowserRouter>
  );
}
