import React, { useState } from "react";
import axios from "axios";
import './App.css';

const App = () => {
    const [inputText, setInputText] = useState("");
    const [outputText, setOutputText] = useState("");

    const generateOutput = async () => {

            await axios.post("http://localhost:8000/generate", { input_text: inputText }).then( response => {
                setOutputText(response.data.message);

            }).catch(error => {
                console.error("Error generating output:", error);
            })
    };

    const testServer = async () => {
        try {
            const response = await axios.get('http://localhost:8000/');
            setOutputText(response.data.message);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    return (
        <div className="page-wrapper">
            <h1>Model-Based Output Generator</h1>
            <textarea
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                placeholder="Enter your input here"
                rows={10}
                cols={80}
                style={{ marginBottom: "10px" }}
            />
            <button onClick={generateOutput}>Generate Output</button>
            <button onClick={testServer}>Test Server</button>
            <textarea
                value={outputText}
                readOnly
                placeholder="Generated output will appear here"
                rows={25}
                cols={80}
                style={{ marginTop: "10px" }}
            />
        </div>
    );
};

export default App;
