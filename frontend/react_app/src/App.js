import React from "react";
import Urls from "./Urls";
import Layout from "./components/Layout";
import { connect } from "react-redux";
import * as actions from "./store/authActions";
import { BrowserRouter, Switch, Route, useParams } from "react-router-dom";
import { useSelector } from "react-redux";
import "./css/app.css";
function App(props) {
  // Similar to componentDidMount and componentDidUpdate:
  React.useEffect(() => {
    props.setAuthenticatedIfRequired();
  });

  // // const params = useParams();
  // const history = useHistory();

  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Layout {...props}>
            <Urls {...props} />
          </Layout>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

//This means that one or more of the redux states in the store are available as props
const mapStateToProps = (state) => {
  return {
    isAuthenticated:
      state.auth.token !== null && typeof state.auth.token !== "undefined",
    token: state.auth.token,
  };
};

//This means that one or more of the redux actions in the form of dispatch(action) combinations are available as props
const mapDispatchToProps = (dispatch) => {
  return {
    setAuthenticatedIfRequired: () => dispatch(actions.authCheckState()),
    logout: () => dispatch(actions.authLogout()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(App);
