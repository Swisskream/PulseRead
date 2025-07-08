import React, {useEffect, useState} from 'react';
import axios from 'axios';

function SummaryList() {
    const [summaries, setSummaries] = useState([]);

    useEffect(() => {
        async function fetchSummaries() {
            const res = await axios.get('https://78uh12wvn2.execute-api.us-west-2.amazonaws.com/prod/get-summaries');
            setSummaries(res.data);
        }

        fetchSummaries();
    }, []);

    return (
        <div>
            <h2>Summary History</h2>
            {summaries.map((item) => (
                <div key={item.id} style={{border: '1px solid #ccc', padding: '1rem', marginBottom: '1rem'}}>
                    <h4>{item.source_file}</h4>
                    <p><strong>Summary:</strong> {item.summary}</p>
                    <p><strong>Time:</strong> {item.timestamp}</p>
                </div>
            ))}
        </div>
    );
}

export default SummaryList;