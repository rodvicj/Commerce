import { useState } from "react";
import { getCookie } from "../getCookie";
import { createGlobalState } from "react-hooks-global-state";

const { useGlobalState, getGlobalState, setGlobalState } = createGlobalState({
  jwtToken: "",
});

export const getJWTToken = () => getGlobalState("jwtToken");
const setJWTToken = (value) => setGlobalState("jwtToken", value);
export const useJWTToken = () => useGlobalState("jwtToken");

// TODO: create LoginPage, and authentication component;
export const Login = () => {
  const [JWT, setJWT] = useJWTToken();
  const [state, setState] = useState({
    username: "",
    password: "",
    // token: "",
  });

  // const [user, setUser] = useState(null);

  const fetchUser = async () => {
    const csrftoken = getCookie("csrftoken");

    try {
      const response = await fetch("http://127.0.0.1:8000/api/login", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
          username: state.username,
          password: state.password,
        }),
      });
      const result = await response.json();
      // setJWTToken(result.authentication);
      setJWT(result.authentication);
      console.log("result complete:", result);
      // return result.authentication.access_token;
    } catch (error) {
      Promise.reject(error);
      console.log("Error:", error);
    }
  };

  const showToken = () => {
    const token = getJWTToken();
    console.log("access token", token?.access_token);
    console.log("refresh token", token?.refresh_token);
  };

  return (
    <div style={{ padding: "10px" }}>
      {JWT ? <p>{JWT.access_token}</p> : <p>Login first</p>}
      <div>
        {/* username:{" "} */}
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
        {/* password:{" "} */}
        <input
          placeholder="password"
          type="text"
          onChange={(event) =>
            setState({ ...state, password: event.target.value })
          }
        />
      </div>
      <button onClick={fetchUser}>Login</button>
      <button onClick={showToken}>showToken</button>
    </div>
  );
};
