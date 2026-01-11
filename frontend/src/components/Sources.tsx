import {Box, IconButton, Link, List, ListItem, Typography} from "@mui/material";
import type { Source } from "../api.ts";
import { MarkdownText } from "./MarkdownText.tsx";
import LaunchIcon from '@mui/icons-material/Launch';
import {useState} from "react";
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';

type Props = {
    sources: Source[];
};

export const Sources = ({ sources }: Props) => {
    return (
        <Box sx={{ mt: 1 }}>
            <Typography variant="caption" color="text.secondary">
                Źródła:
            </Typography>
            <List sx={{ pl: 2, mt: 0 }}>
                {sources.map((s, i) => (
                    <ListItem key={s.id ?? i} sx={{ py: 0 }}>
                        <SourceItem source={s} idx={i} />
                    </ListItem>
                ))}
            </List>
        </Box>
    );
};

type ItemProps = {
    source: Source;
    idx: number;
};

const SourceItem = ({ source, idx }: ItemProps) => {
    const [collapsed, setCollapsed] = useState(true);

    return (
        <Box>
            <Typography variant="h6">
                [{idx + 1}] {source.title ?? source.id ?? "source"}
                <Link target="_blank" href={buildSourceLink(source)}><LaunchIcon/></Link>
            </Typography>
            <IconButton onClick={() => setCollapsed(!collapsed)} >
                {collapsed ? <KeyboardArrowRightIcon/> : <KeyboardArrowDownIcon/>}
            </IconButton>
            <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5, display: collapsed ? 'none' : 'block' }}>
                <MarkdownText text={source.content} />
            </Typography>
        </Box>
    );
};

const buildSourceLink = (source: Source) => {
    const notesBaseUrl = "https://mgarbowski.github.io/notes.mgarbowski.pl"
    return `${notesBaseUrl}/${source.course}/${source.filename}`
}
