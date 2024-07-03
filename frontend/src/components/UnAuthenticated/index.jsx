import { useState } from "react";
import useClient from "../Client";

import "./styles.css";

const UnAuthenticated = () => {
  const { login } = useClient();

  const [state, setState] = useState({
    username: "",
    password: "",
  });

  return (
    <>
      <div className="login__container">
        <input
          className="login__username"
          placeholder="username"
          label="username"
          type="text"
          onChange={(event) =>
            setState({ ...state, username: event.target.value })
          }
        />
        <input
          className="login__password"
          placeholder="password"
          type="password"
          onChange={(event) =>
            setState({ ...state, password: event.target.value })
          }
        />
        <input
          className="login__button"
          type="button"
          onClick={() => login(state.username, state.password)}
          value="Login"
        />
      </div>
    </>
  );
};

export default UnAuthenticated;
