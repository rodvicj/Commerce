import { useClient } from "../Client";
import "./styles.css";

export const Header = () => {
  // const { logout, user } = useClient();
  const { logout, user } = useClient();

  return (
    <>
      <div className="header__container">
        <p className="header__username">{user.username}</p>
        <ul className="header__nav-container">
          <li className="header__nav-items">Home</li>
          <li className="header__nav-items">Products</li>
        </ul>
        <button className="header__logout-btn" onClick={() => logout()}>
          Logout
        </button>
      </div>
    </>
  );
};

export default Header;
