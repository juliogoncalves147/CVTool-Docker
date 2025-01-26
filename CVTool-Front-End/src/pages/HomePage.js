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
import homeImage from '../images/home.png';

const theme = createTheme({
  palette: {
    primary: {
      main: "#004643",
    },
    secondary: {
      main: "#FAF4D3",
    },
    background: {
      default: "#0C1618", // Main background color
    },
    text: {
      primary: "#FAF4D3", // Main text color
      secondary: "#FAF4D3", // Accent text color
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
        sx={{ background: "#0C1618" }}
      >
        <Toolbar>
          <Typography variant="h5"color="textSecondary" style={{ flexGrow: 1 }}>
            Resume Management Tool for LaTeX
          </Typography>
          <ScrollLink to="section1" smooth={true} duration={500}>
          <Button color="secondary" sx={{ color: "#FAF4D3" }}>
            Home Page
          </Button>
        </ScrollLink>

        <Button
               color="secondary" sx={{ color: "#FAF4D3" }}
              href="/tool"
            >
              Tool
            </Button>

        {/* Features Button */}
        <ScrollLink to="section2" smooth={true} duration={500}>
          <Button color="secondary" sx={{ color: "#FAF4D3" }}>
            Features
          </Button>
        </ScrollLink>

        {/* Documentation Button */}
        <ScrollLink to="section3" smooth={true} duration={500}>
          <Button color="secondary" sx={{ color: "#FAF4D3" }}>
            Documentation
          </Button>
        </ScrollLink>
        </Toolbar>
      </AppBar>
      <Container 
  maxWidth={false} 
  sx={{ width: "100%", background: "#0C1618", padding: 0 }}
>
  <Element name="section1" className="element">
  <Grid
  container
  spacing={0}
  alignItems="center"
  sx={{
    minHeight: "100vh", 
  }}
>
      {/* Left Side Content */}
      <Grid 
    item 
    xs={12} 
    md={6}
    sx={{
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      p: { xs: 2, md: 6 },
    }}
  >
    <Box 
      textAlign="left" 
      maxWidth="500px"
    >
          <Typography variant="h1" color="textSecondary" gutterBottom>
            Welcome to the Resume Management Tool
          </Typography>
          <Typography variant="h2" color="primary" gutterBottom>
            Simplify Your Resume Creation
          </Typography>
          <Typography variant="body1" color="textSecondary" gutterBottom>
            Manage and generate LaTeX resumes in seconds. Start now to
            take control of your professional documents with ease.
          </Typography>
          <Box mt={4} display="flex" gap={2}>
            <Button
              variant="contained"
              color="primary"
              size="large"
              href="/tool"
            >
              Try Now
            </Button>
            <ScrollLink to="section2" smooth duration={1000}>
              <Button variant="outlined" color="primary" size="large">
                Learn More
              </Button>
            </ScrollLink>
          </Box>
        </Box>
      </Grid>

      {/* Right Side Image */}
      <Grid 
    item 
    xs={12} 
    md={6} 
    sx={{
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      p: { xs: 2, md: 6 },
    }}
  >
    <Box 
      component="img"
      src={homeImage}
      alt="Professional Resume Illustration"
      sx={{
        width: "100%",
        maxWidth: "500px",
        borderRadius: "8px",
        boxShadow: "0 8px 16px rgba(0, 0, 0, 0.2)",
        animation: "fadeIn 1.5s ease",
      }}
    />
  </Grid>
    </Grid>
  </Element>
</Container>


        <Container maxWidth="lg">

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
                    color="primary"
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
                    color="primary"
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
                    Theme Filter
                  </Typography>
                  <Typography
                    variant="body1"
                    color="primary"
                    textAlign="justify"
                    sx={{ flexGrow: 1 }}
                  >
                     Simplify your resume customization with the keyword filter.
                    Set a specific keyword, and seamlessly identify and highlight relevant tokens of your resume. 
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
                    color="primary"
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
                    SubSection Filter
                  </Typography>
                  <Typography
                    variant="body1"
                    color="primary"
                    textAlign="justify"
                    sx={{ flexGrow: 1 }}
                  >
                    Streamline your resume by subsection. Customize your resume by
                    applying filters to specified subsections.
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
                    color="primary"
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
        </Container>
        <Container>
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
                  <Typography variant="body1" color="primary">
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
    <Typography variant="body1" color="primary">
      The Domain-Specific Language (DSL) defined by us provides a structured way to query and manipulate resumes using specific commands. It allows users to perform operations such as selecting sections, filtering by criteria like dates or themes, translating content into different languages, exporting data, and reordering resume sections. The DSL aims to simplify the management and customization of resumes by offering a clear syntax for executing these tasks efficiently.
    </Typography>
    <Typography variant="h5" color="primary" gutterBottom style={{ marginTop: "1.5rem" }}>
      Query Examples
    </Typography>
    <Typography variant="body1" color="primary">
      <p>
        <strong>Example 1:</strong> Selecting specific sections
      </p>
      <p>
        <span className="query-command"> Show </span> 
        <span className="query-parameter"> 'Work experience', 'Education' </span>
        <br />
        -- Returns only the sections 'Work experience' and 'Education'
      </p>
      <br />
      <p>
        <strong>Example 2:</strong> Selecting all sections
      </p>
      <p>
        <span className="query-command"> Show </span> 
        <span className="query-parameter"> * </span>
        <br />
        -- Returns all sections
      </p>
      <br />
      <p>
        <strong>Example 3:</strong> Filtering a specific section by date
      </p>
      <p>
        <span className="query-command"> Show </span> 
        <span className="query-parameter"> * </span> 
        <span className="query-command"> Filtered By </span> 
        <span className="query-parameter">SECTION = 'Education' AND DATE >= '2010'</span>
        <br />
        -- Returns the entire file, filtering the 'Education' section by date
      </p>
      <br />
      <p>
        <strong>Example 4:</strong> Filtering multiple sections by different dates
      </p>
      <p>
        <span className="query-command"> Show </span> 
        <span className="query-parameter"> * </span>
        <span className="query-command"> Filtered By </span>
        <span className="query-parameter"> (section = 'Education Universitary' AND DATE > '2010') OR (subsection = 'Chair person' AND DATE = '2010')</span>
        <br />
        -- Returns the entire file, filtering specified sections by different dates
      </p>
      <br />
      <p>
        <strong>Example 5:</strong> Filtering the entire file by date
      </p>
      <p>
        <span className="query-command"> Show </span> 
        <span className="query-parameter"> * </span>
        <span className="query-command"> Filtered By </span>
        <span className="query-parameter"> DATE > '2010'</span>
        <br />
        -- Returns the entire file, filtering by date
      </p>
      <br />
      <p>
        <strong>Example 6:</strong> Filtering the entire file by date, except for a specific section
      </p>
      <p>
        <span className="query-command"> Show </span> 
        <span className="query-parameter"> * </span>
        <span className="query-command"> Filtered By </span> 
        <span className="query-parameter"> SECTION != 'Education' and DATE > '2010' </span>
        <br />
        -- Returns the entire file, filtering by date, excluding the 'Education' section
      </p>
      <br />
      <p>
        <strong>Example 7:</strong> Filtering file for specific sections and date
      </p>
      <p>
       <span className="query-command"> Show </span>  
        <span className="query-parameter">'Professional Experience', 'Education' </span> 
        <span className="query-command"> Filtered By </span>  
        <span className="query-parameter"> DATE > '2010' </span>
        <br />
        -- Returns only the sections 'Professional Experience' and 'Education' with dates greater than 2010
      </p>
      <br />
      <p>
        <strong>Example 8:</strong> Selecting specific sections, filtering subsection for date
      </p>
      <p>
       <span className="query-command"> Show </span>  
        <span className="query-parameter">'Professional Experience', 'Education' </span> 
        <span className="query-command"> Filtered By </span>  
        <span className="query-parameter"> subsection = 'Chair person' and date > '2010' </span>
        <br />
        -- Returns only the sections 'Professional Experience' and 'Education' filtering the subsection 'Chair person' by date
      </p>
      <br />
      <p>
        <strong>Example 9:</strong> Translating resume into another language
      </p>
      <p>
        <span className="query-command"> TRANSLATE FROM </span>
        <span className="query-parameter"> 'fr' ;</span>
        <span className="query-command"> TO </span>
        <span className="query-parameter"> 'en' ;</span>
        <br />
        -- Translates the resume from French to English
      </p>
      <br />
      <p>
        <strong>Example 10:</strong> Reordering sections
      </p>
      <p>
        <span className="query-command"> REORDER </span>
        <span className="query-parameter"> 'Professional Experience', 'Education', 'Projects'</span>
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
            <Typography variant="body1" color="primary" paragraph>
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
          <Typography variant="body2" color="primary">
            © 2024 Júlio Gonçalves. All rights reserved.
          </Typography>
          <Button
            color="inherit"
            href="https://www.linkedin.com/in/juliogoncalvess/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <LinkedInIcon />
          </Button>
          <Button
            color="inherit"
            href="https://github.com/juliogoncalves147"
            target="_blank"
            rel="noopener noreferrer"
          >
            <GitHubIcon />
          </Button>
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default HomePage;
