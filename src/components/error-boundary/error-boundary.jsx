import React from "react";
import Alert from 'react-bootstrap/Alert';
<<<<<<< HEAD
import { Link } from "react-router-dom";
=======
>>>>>>> f393bfd59599422952d99ac5209358fb674fd1f3

class ErrorBoundary extends React.Component {

    state = {
        hasError: false,
    }

    componentDidCatch() {
        return this.setState({ hasError: true });
    }

    render() {
        if (this.state.hasError) {
            return <Alert variant="danger">
<<<<<<< HEAD
                Something went wrong! <span>go back<Link to={"/"} reloadDocument className="text-decoration-none"> home</Link></span>
=======
                Something went wrong!
>>>>>>> f393bfd59599422952d99ac5209358fb674fd1f3
            </Alert>
            // return <p>Something went wrong</p>
            // return this.props.fallback;
        }
        return this.props.children;
    }
}

export { ErrorBoundary };