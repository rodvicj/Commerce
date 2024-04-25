import { useCallback } from "react";
import { createGlobalState } from "react-hooks-global-state";
// import axios from "axios";
import { getCookie } from "../getCookie";

// const { useGlobalState, getGlobalState, setGlobalState } = createGlobalState({
const { useGlobalState } = createGlobalState({
  jwtToken: "",
});
// const getJWTToken = () => getGlobalState("jwtToken");
// const setJWTToken = value => setGlobalState("jwtToken", value);
const useJWTToken = () => useGlobalState("jwtToken");

export function useClient() {
  const [JWT, setJWT] = useJWTToken();

  const login = useCallback(async (name, password) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/login", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie(),
        },
        body: JSON.stringify({
          username: name,
          password: password,
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
  }, []);

  const logout = useCallback(() => {
    setJWT("");
  }, []);

  // const getTodos = useCallback(
  //   () =>
  //     client
  //       .post("/", { query: "query { todos }" }, { withCredentials: true })
  //       .then(({ data }) => data.data.todos),
  //   [],
  // );

  return {
    JWT,
    // getTodos,
    login,
    logout,
  };
}

// export default client;
