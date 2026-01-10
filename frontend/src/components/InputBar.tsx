import { Box, Button, TextField } from "@mui/material";
import type React from "react";

type Props = {
    value: string;
    onChange: (v: string) => void;
    onSend: () => void;
    disabled?: boolean;
    onKeyDown?: (e: React.KeyboardEvent<HTMLDivElement>) => void;
};

export const InputBar: React.FC<Props> = ({
    value,
    onChange,
    onSend,
    disabled,
    onKeyDown,
}) => {
    return (
        <Box
            component="form"
            onSubmit={(e) => {
                e.preventDefault();
                if (!disabled) onSend();
            }}
            sx={{ mt: 2, display: "grid", gap: 1 }}
        >
            <TextField
                multiline
                minRows={3}
                value={value}
                onChange={(e) => onChange(e.target.value)}
                placeholder="Zadaj pytanie..."
                onKeyDown={onKeyDown}
                fullWidth
            />
            <Box sx={{ display: "flex", justifyContent: "flex-end" }}>
                <Button
                    variant="contained"
                    onClick={onSend}
                    disabled={disabled}
                >
                    Wyślij
                </Button>
            </Box>
        </Box>
    );
};
