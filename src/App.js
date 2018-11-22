import React, {Component} from 'react';
import {Box, Grommet, Heading, ResponsiveContext} from 'grommet';
import LikedShowsList from './components/layout/LikedShowsList';

const theme = {
  global: {
    colors: {
      brand: '#228BE6'
    },
    font: {
      family: 'Lato',
      size: '14px',
      height: '20px'
    }
  }
};

const AppBar = (props) => (
  <Box
    tag='header'
    direction='row'
    align='center'
    justify='between'
    background='brand'
    pad={{left: 'medium', right: 'small', vertical: 'small'}}
    elevation='medium'
    style={{zIndex: '1'}}
    {...props}
  />
);

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      shows: []
    };
  }

  async componentDidMount() {
    // const shows = await loadFile('shows.txt');
    const shows = await (await fetch('shows.txt')).text();
    this.setState({
      loading: false,
      shows: shows.split('\n')
    });
  }

  render() {
    return (
      <Grommet theme={theme}>
        <ResponsiveContext.Consumer>
          {size => (
            <Box fill>
              <AppBar>
                <Heading level='3' margin='small'>My App</Heading>
              </AppBar>
              <Box margin='medium'>
                <LikedShowsList showList={this.state.shows}/>
              </Box>
            </Box>
          )}
        </ResponsiveContext.Consumer>
      </Grommet>
    );
  }
}

export default App;
