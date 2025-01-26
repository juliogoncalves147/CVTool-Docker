import React from "react";
import { Typography, Link, IconButton } from "@mui/material";
import { GitHub, LinkedIn } from "@mui/icons-material";
import { styled } from "@mui/system";

const FooterContainer = styled("footer")({
  background: "#0C1618",
  color: "#FAF4D3",
  padding: "20px",
  textAlign: "center",
  position: "relative",
  bottom: 0,
  width: "100%",
  overflow: "hidden",
  maxHeight: "12vh",
});

const Footer = () => {
  return (
    <FooterContainer>
      <Typography variant="body1">
        © {new Date().getFullYear()} Júlio Gonçalves.
      </Typography>
      <Typography variant="body2">All rights reserved.</Typography>
      <div>
        <IconButton
          color="inherit"
          component={Link}
          href="https://github.com/juliogoncalves147"
        >
          <GitHub />
        </IconButton>
        <IconButton
          color="inherit"
          component={Link}
          href="https://www.linkedin.com/in/juliogoncalvess/"
        >
          <LinkedIn />
        </IconButton>
      </div>
    </FooterContainer>
  );
};

export default Footer;
