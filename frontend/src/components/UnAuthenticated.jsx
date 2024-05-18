import { useState } from "react";
import { useClient } from "./Client";

const UnAuthenticated = () => {
  const { login } = useClient();

  const [state, setState] = useState({
    username: "",
    password: "",
  });

  return (
    <>
      <div>
        <input
          placeholder="username"
          label="username"
          type="text"
          onChange={(event) =>
            setState({ ...state, username: event.target.value })
          }
        />
      </div>
      <div>
        <input
          placeholder="password"
          type="text"
          onChange={(event) =>
            setState({ ...state, password: event.target.value })
          }
        />
      </div>
      <button onClick={() => login(state.username, state.password)}>
        Login
      </button>
    </>
  );
};

export default UnAuthenticated;
