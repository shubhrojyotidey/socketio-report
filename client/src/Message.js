export const Message = ({ message }) => {
    if (message.type === 'join') return <p>{`${message.sid} joined in`}</p>;
    if (message.type === 'chat') return <p>{`${message.sid}: ${message.message}`}</p>;
  };  