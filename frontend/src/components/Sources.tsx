import {Box, Link, List, ListItem, Typography} from "@mui/material";
import type { Source } from "../api.ts";
import { MarkdownText } from "./MarkdownText.tsx";
import LaunchIcon from '@mui/icons-material/Launch';

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
    const content =
        source.content.length > 220
            ? `${source.content.slice(0, 220)}…`
            : source.content;
    return (
        <Box>
            <Typography variant="h5">
                [{idx + 1}] {source.title ?? source.id ?? "source"}
                <Link target="_blank" href={buildSourceLink(source)}><LaunchIcon/></Link>
            </Typography>
            <Typography variant="body2" color="text.secondary">
                <MarkdownText text={content} />
            </Typography>
        </Box>
    );
};

const buildSourceLink = (source: Source) => {
    const notesBaseUrl = "https://mgarbowski.github.io/notes.mgarbowski.pl"
    return `${notesBaseUrl}/${source.course}/${source.filename}`
}
