import { useClient } from "./components/Client";
import Authenticated from "./components/Authenticated";
import UnAuthenticated from "./components/UnAuthenticated";

function App() {
  const { JWT } = useClient();

  return <>{JWT ? <Authenticated /> : <UnAuthenticated />}</>;
}

export default App;
