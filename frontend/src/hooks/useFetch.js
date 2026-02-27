import { useEffect, useState } from "react";

export default function useFetch(fetchFunction, params = []) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function execute() {
      try {
        const result = await fetchFunction();
        setData(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    execute();
  }, params);

  return { data, loading, error };
}
