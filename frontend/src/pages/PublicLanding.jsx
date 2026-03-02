import { useParams } from "react-router-dom";
import { getPublicGym } from "../api/PublicApi";
import PageWrapper from "../components/layout/PageWrapper";
import GymHeader from "../components/gym/GymHeader";
import RoutineSelector from "../components/routine/RoutineSelector";
import useFetch from "../hooks/useFetch";
import Loader from "../components/ui/Loader";
import ErrorMessage from "../components/ui/ErrorMessage";

export default function PublicLanding() {
  const { qr_token } = useParams();

  const { data, loading, error } = useFetch(
    () => getPublicGym(qr_token),
    [qr_token],
  );

  if (loading) return <Loader />;
  if (error) return <ErrorMessage message={error} />;

  return (
    <PageWrapper gym={data.gym}>
      <GymHeader gym={data.gym} />
      <RoutineSelector qrToken={qr_token} routines={data.rutinas_disponibles} />
    </PageWrapper>
  );
}
