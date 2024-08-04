import React from "react";
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Container,
  Box,
  Grid,
  Paper,
} from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import GitHubIcon from "@mui/icons-material/GitHub";
import { Link as ScrollLink, Element } from "react-scroll";
import "./HomePage.css";

const theme = createTheme({
  palette: {
    primary: {
      main: "#1976d2",
    },
    secondary: {
      main: "#fff",
    },
  },
  typography: {
    h1: {
      fontSize: "3rem",
      fontWeight: 700,
      marginBottom: "1rem",
    },
    h2: {
      fontSize: "2rem",
      fontWeight: 500,
      marginBottom: "1rem",
    },
    body1: {
      fontSize: "1.25rem",
      marginBottom: "1.5rem",
    },
    button: {
      fontSize: "1rem",
      fontWeight: 600,
    },
  },
});

function HomePage() {
  return (
    <ThemeProvider theme={theme}>
      <AppBar
        position="sticky"
        sx={{ background: "linear-gradient(to right, #0d47a1, #42a5f5)" }}
      >
        <Toolbar>
          <Typography variant="h6" style={{ flexGrow: 1 }}>
            Resume Management Tool for LaTeX
          </Typography>
          <Button
            color="inherit"
            href="https://www.linkedin.com/in/yourprofile"
            target="_blank"
            rel="noopener noreferrer"
          >
            <LinkedInIcon />
          </Button>
          <Button
            color="inherit"
            href="https://github.com/yourprofile"
            target="_blank"
            rel="noopener noreferrer"
          >
            <GitHubIcon />
          </Button>
        </Toolbar>
      </AppBar>
      <Container maxWidth="lg">
        <Element name="section1" className="element">
          <Box
            display="flex"
            flexDirection="column"
            alignItems="center"
            justifyContent="center"
            height="100vh"
            textAlign="center"
            background="linear-gradient(to right, #0d47a1, #42a5f5)"
          >
            <Typography variant="h1" color="primary">
              Welcome to the Resume Management Tool for LaTeX
            </Typography>
            <Typography variant="h2" color="textSecondary">
              Simplify your resume creation process with our tool
            </Typography>
            <Typography
              variant="body1"
              color="textSecondary"
              sx={{
                whiteSpace: "nowrap",
                overflow: "hidden",
                textOverflow: "ellipsis",
              }}
            >
              Our tool helps you manage and generate new Latex CVs in seconds.
              Start exploring now!
            </Typography>
            <div
              style={{ display: "flex", justifyContent: "center", gap: "1rem" }}
            >
              <Button
                variant="contained"
                color="primary"
                size="large"
                href="/tool"
              >
                Try now
              </Button>
              <ScrollLink
                to="section2"
                smooth
                duration={1000}
                style={{ textDecoration: "none" }}
              >
                <Button variant="contained" color="primary" size="large">
                  Learn More
                </Button>
              </ScrollLink>
            </div>
          </Box>
        </Element>

        <Element name="section2" className="element">
          <Box mt={5} py={5} textAlign="center">
            <Typography variant="h2" color="primary" gutterBottom>
              Key Features
            </Typography>
            <Grid container spacing={4} justifyContent="center">
              <Grid item xs={12} sm={6} md={4}>
                <Paper
                  elevation={3}
                  sx={{
                    padding: "2rem",
                    textAlign: "left",
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                  }}
                >
                  <Typography variant="h5" color="primary" gutterBottom>
                    Translate Filter
                  </Typography>
                  <Typography
                    variant="body1"
                    color="textSecondary"
                    textAlign="justify"
                    sx={{ flexGrow: 1 }}
                  >
                    Easily translate your resume into multiple languages with a
                    single click. Our tool integrates seamlessly with Google
                    Translate API, ensuring accuracy and efficiency.
                  </Typography>
                </Paper>
              </Grid>
              <Grid item xs={12} sm={6} md={4}>
                <Paper
                  elevation={3}
                  sx={{
                    padding: "2rem",
                    textAlign: "left",
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                  }}
                >
                  <Typography variant="h5" color="primary" gutterBottom>
                    Date Filter
                  </Typography>
                  <Typography
                    variant="body1"
                    color="textSecondary"
                    textAlign="justify"
                    sx={{ flexGrow: 1 }}
                  >
                    Filter your resume by date effortlessly. Manage different
                    versions and track career progression with ease, generating
                    customized resumes based on specific timeframes.
                  </Typography>
                </Paper>
              </Grid>
              <Grid item xs={12} sm={6} md={4}>
                <Paper
                  elevation={3}
                  sx={{
                    padding: "2rem",
                    textAlign: "left",
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                  }}
                >
                  <Typography variant="h5" color="primary" gutterBottom>
                    Section Filter
                  </Typography>
                  <Typography
                    variant="body1"
                    color="textSecondary"
                    textAlign="justify"
                    sx={{ flexGrow: 1 }}
                  >
                    Streamline your resume by section. Customize your resume by
                    selecting only the relevant sections, enhancing clarity and
                    relevance.
                  </Typography>
                </Paper>
              </Grid>
              <Grid item xs={12} sm={6} md={4}>
                <Paper
                  elevation={3}
                  sx={{
                    padding: "2rem",
                    textAlign: "left",
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                  }}
                >
                  <Typography variant="h5" color="primary" gutterBottom>
                    Reorder Filter
                  </Typography>
                  <Typography
                    variant="body1"
                    color="textSecondary"
                    textAlign="justify"
                    sx={{ flexGrow: 1 }}
                  >
                    Arrange resume sections effortlessly. Rearrange your resume
                    sections as needed to emphasize key strengths and
                    experiences.
                  </Typography>
                </Paper>
              </Grid>
            </Grid>
          </Box>
        </Element>

        <Element name="section3" className="element">
          <Box mt={5} py={5} textAlign="center">
            <Typography variant="h2" color="primary" gutterBottom>
              Documentation
            </Typography>
            <Grid container spacing={4} justifyContent="center">
              {/* Part 1: Restrictions */}
              <Grid item xs={12}>
                <Paper
                  elevation={3}
                  sx={{
                    padding: "2rem",
                    textAlign: "left",
                    width: "100%",
                    maxWidth: "1200px",
                    margin: "0 auto",
                  }}
                >
                  <Typography variant="h5" color="primary" gutterBottom>
                    Restrictions
                  </Typography>
                  <Typography variant="body1" color="textSecondary">
                    <ol>
                      <li>Sem comentarios</li>
                      <li>Parentises todos espaçados ?</li>
                      <li>
                        Ter cuidado com as secções que manda traduzir por causa
                        de referencias.
                      </li>
                      <li>
                        Para o filtro das sections funcionar direito, os nomes
                        das sections tem que ter texto limpo, sem comandos pelo
                        meio do tipo "\comando"
                      </li>
                      <li>
                        Para o filtro das datas funcionar, o utilizador deve
                        adicionar o seguinte comando no inicio do curriculo:{" "}
                        <code>{"\\newcommand{\\daterange}[1]{#1}"}</code>
                        <br></br>
                        Todas as datas devem estar definidas usando este
                        comando, para o filtro funcionar corretamente. Exemplo:{" "}
                        <code>{"\\daterange{2014-2020}"}</code>
                      </li>
                    </ol>
                  </Typography>
                </Paper>
              </Grid>

              {/* Part 2: DSL Explanation and Query Examples */}
              <Grid item xs={12}>
                <Paper
                  elevation={3}
                  sx={{
                    padding: "2rem",
                    textAlign: "left",
                    width: "100%",
                    maxWidth: "1200px",
                    margin: "0 auto",
                  }}
                >
                  <Typography variant="h5" color="primary" gutterBottom>
                    DSL (Domain-Specific Language) Explanation
                  </Typography>
                  <Typography variant="body1" color="textSecondary">
                    The Domain-Specific Language (DSL) defined by us provides a
                    structured way to query and manipulate resumes using
                    specific commands. It allows users to perform operations
                    such as selecting sections, filtering by criteria like dates
                    or themes, translating content into different languages,
                    exporting data, and reordering resume sections. The DSL aims
                    to simplify the management and customization of resumes by
                    offering a clear syntax for executing these tasks
                    efficiently.
                  </Typography>
                  <Typography
                    variant="h5"
                    color="primary"
                    gutterBottom
                    style={{ marginTop: "1.5rem" }}
                  >
                    Query Examples
                  </Typography>
                  <Typography variant="body1" color="textSecondary">
                    <p>
                      <strong>Example 1:</strong> Selecting specific sections
                    </p>
                    <p>
                      SELECT 'Work experience', 'Education'
                      <br />
                      -- Returns only the sections 'Work experience' and
                      'Education'
                    </p>
                    <br />
                    <p>
                      <strong>Example 2:</strong> Selecting all sections
                    </p>
                    <p>
                      SELECT *<br />
                      -- Returns all sections
                    </p>
                    <br />
                    <p>
                      <strong>Example 3:</strong> Filtering a specific section
                      by date
                    </p>
                    <p>
                      SELECT * WHERE SECTION = 'Education' AND DATE >= '2010'
                      <br />
                      -- Returns the entire file, filtering the 'Education'
                      section by date
                    </p>
                    <br />
                    <p>
                      <strong>Example 4:</strong> Filtering multiple sections by
                      different dates
                    </p>
                    <p>
                      SELECT * WHERE (SECTION = 'Education Universitary' AND
                      DATE > '2010') OR (SECTION = 'Professional Experience' AND
                      DATE = '2010')
                      <br />
                      -- Returns the entire file, filtering specified sections
                      by different dates
                    </p>
                    <br />
                    <p>
                      <strong>Example 5:</strong> Filtering the entire file by
                      date
                    </p>
                    <p>
                      SELECT * WHERE DATE > '2010'
                      <br />
                      -- Returns the entire file, filtering by date
                    </p>
                    <br />
                    <p>
                      <strong>Example 6:</strong> Filtering the entire file by
                      date, except for a specific section
                    </p>
                    <p>
                      SELECT * WHERE SECTION != 'Education' AND DATE > '2010'
                      <br />
                      -- Returns the entire file, filtering by date, excluding
                      the 'Education' section
                    </p>
                    <br />
                    <p>
                      <strong>Example 7:</strong> Filtering file for specific
                      sections and date
                    </p>
                    <p>
                      SELECT 'Professional Experience', 'Education' WHERE DATE >
                      '2010'
                      <br />
                      -- Returns only the sections 'Professional Experience' and
                      'Education' with dates greater than 2010
                    </p>
                    <br />
                    <p>
                      <strong>Example 8:</strong> Translating resume into
                      another language
                    </p>
                    <p>
                      TRANSLATE FROM 'fr' TO 'en';
                      <br />
                      -- Translates the resume from French to English
                    </p>
                    <br />
                    <p>
                      <strong>Example 9:</strong> Reordering sections
                    </p>
                    <p>
                      REORDER "Professional Experience", "Education", "Projects"
                      <br />
                      -- Reorders the sections of the resume as specified
                    </p>
                  </Typography>
                </Paper>
              </Grid>
            </Grid>
          </Box>
        </Element>

        <Element name="section4" className="element">
          <Box mt={5} py={5} textAlign="center">
            <Typography variant="h2" color="primary">
              Try Now!
            </Typography>
            <Typography variant="body1" color="textSecondary" paragraph>
              Upload your LaTeX resume file and see the magic happen. Our tool
              will process your file and provide you a simple query language to
              manage your resume.
            </Typography>
            <Button
              variant="contained"
              color="primary"
              size="large"
              href="/tool"
            >
              Go to Tool
            </Button>
          </Box>
        </Element>
        <Box mt={5} textAlign="center">
          <Typography variant="body2" color="textSecondary">
            © 2024 Your Company Name. All rights reserved.
          </Typography>
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default HomePage;
