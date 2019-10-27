import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { ModalProvider } from "react-modal-hook";
import { TransitionGroup } from "react-transition-group";
import App from './App';

ReactDOM.render(
    <ModalProvider container={TransitionGroup}>
        <App />
    </ModalProvider>,
    document.getElementById('root'));
