import { useCallback } from "react";
import { createGlobalState } from "react-hooks-global-state";
import getCookie from "../Cookie";

const { useGlobalState } = createGlobalState({
  jwtToken: "",
  user: "",
});

const useJWTToken = () => useGlobalState("jwtToken");
const useUser = () => useGlobalState("user");

export function useClient() {
  const [JWT, setJWT] = useJWTToken();
  const [user, setUser] = useUser();

  const login = useCallback(async (name, password) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/login", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({
          username: name,
          password: password,
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
  }, []);

  const logout = useCallback(() => {
    setJWT("");
    setUser({});
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
    user,
    login,
    logout,
  };
}

export default useClient;
