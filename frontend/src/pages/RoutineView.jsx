import { useParams } from "react-router-dom";
import { getRoutine } from "../api/PublicApi";
import PageWrapper from "../components/layout/PageWrapper";
import GymHeader from "../components/gym/GymHeader";
import RoutineCard from "../components/routine/RoutineCard";
import useFetch from "../hooks/useFetch";
import Loader from "../components/ui/Loader";
import ErrorMessage from "../components/ui/ErrorMessage";

export default function RoutineView() {
  const { qr_token, type } = useParams();

  const { data, loading, error } = useFetch(
    () => getRoutine(qr_token, type),
    [qr_token, type],
  );

  if (loading) return <Loader />;
  if (error) return <ErrorMessage message={error} />;

  return (
    <PageWrapper gym={data.gym}>
      <GymHeader gym={data.gym} />
      <RoutineCard type={data.type} exercises={data.routine} />
    </PageWrapper>
  );
}
