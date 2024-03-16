import { useState } from "react";
import getCookie from "../getCookie";

const Login = () => {
  const [state, setState] = useState({
    username: "",
    password: "",
    token: "",
  });

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
      setState({ ...state, token: result.authentication.access_token });
      console.log("result:",result);
    } catch (error) {
      console.log("Error:", error);
    }
  };

  return (
    <div>
      <input
        type="text"
        onChange={(event) =>
          setState({ ...state, username: event.target.value })
        }
      />
      <input
        type="text"
        onChange={(event) =>
          setState({ ...state, password: event.target.value })
        }
      />
      <button onClick={fetchUser}>click me</button>
    </div>
  );
};

export default Login;
