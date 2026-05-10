// Create a style element
const style = document.createElement('style');
style.textContent = `
    h1 {
        animation: slideIn 1s ease-in-out;
    }

    @keyframes slideIn {
        from {
            transform: translateX(-100px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
`;

document.head.appendChild(style);