import { useClient } from "./components/Client";
import Authenticated from "./components/Authenticated";
import UnAuthenticated from "./components/UnAuthenticated";

function App() {
  const { JWT } = useClient();

  return (
    <div className="App" style={{ padding: "10px" }}>
      {JWT ? <Authenticated /> : <UnAuthenticated />}
    </div>
  );
}

export default App;
