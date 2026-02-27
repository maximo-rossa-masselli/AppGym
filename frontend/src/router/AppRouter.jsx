import { BrowserRouter, Routes, Route } from "react-router-dom";
import PublicLanding from "../pages/PublicLanding";
import RoutineView from "../pages/RoutineView";

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
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
