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
  const [user, setUser] = useState(null);
  const [state, setState] = useState({
    username: "",
    password: "",
    // token: "",
  });

  // const [user, setUser] = useState(null);

  const fetchUser = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/login", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({
          username: state.username,
          password: state.password,
        }),
      });
      const result = await response.json();
      // setJWTToken(result.authentication);
      setJWT(result.authentication);
      setUser(result.user);
      console.log("result complete:", result);
      // return result.authentication.access_token;
    } catch (error) {
      Promise.reject(error);
      console.log("Error:", error);
    }
  };

  const logout = () => {
    setJWT(undefined);
    setUser(undefined);
    setState({ username: "", password: "" });
  };

  return (
    <div style={{ padding: "10px" }}>
      {JWT ? (
        <>
          {" "}
          <p>{user.username}</p> <button onClick={logout}>Logout</button>{" "}
        </>
      ) : (
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
        </>
      )}
    </div>
  );
};
