interface TogglerProps {
    isOpen: boolean;
    onChange: (isOpen: boolean) => void;
}

export default function Toggler({ isOpen, onChange: onToggle }: TogglerProps) {
    return (
        <div
            className="ml-auto cursor-pointer"
            onClick={(e) => {
                e.stopPropagation();
                e.preventDefault();
                onToggle(!isOpen);
            }}
        >
            {isOpen ? (
                <svg
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth={1.5}
                    stroke="#1d9bf0"
                    className="p-2 w-8 h-8 rounded hover:bg-blue-50 select-none"
                >
                    <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="M19.5 8.25l-7.5 7.5-7.5-7.5"
                    />
                </svg>
            ) : (
                <svg
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth={1.5}
                    stroke="#1d9bf0"
                    className="p-2 w-8 h-8 rounded hover:bg-blue-50 select-none"
                >
                    <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="M4.5 15.75l7.5-7.5 7.5 7.5"
                    />
                </svg>
            )}
        </div>
    );
}
