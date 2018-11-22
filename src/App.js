import React, {Component} from 'react';
import {Box, Button, Grommet, Heading, Image, Layer, ResponsiveContext} from 'grommet';
import LikedShowsList from './components/layout/LikedShowsList';
import {FormClose} from 'grommet-icons';

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
    height='80px'
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
      showSidebar: false,
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
      <Grommet theme={theme} full>
        <ResponsiveContext.Consumer>
          {size => (
            <Box fill>
              <AppBar>
                <Image id="logo" src="video-camera.svg" fit='contain'/>
                <Heading level='2' margin='small' id='title'>Working Title</Heading>
              </AppBar>
              <Box direction='row' flex fill='vertical'>
                <Box flex margin='medium'>
                  <LikedShowsList showList={this.state.shows}/>
                </Box>
                {(size !== 'small') ? (
                  <Box
                    flex
                    fill='vertical'
                    width='medium'
                    background='light-2'
                    elevation='small'
                    align='center'
                    justify='center'
                  >
                    TODO display similar shows
                  </Box>
                ) : (this.state.showSidebar &&
                  <Layer>
                    <Box
                      background='light-2'
                      tag='header'
                      justify='end'
                      align='center'
                      direction='row'
                    >
                      <Button
                        icon={<FormClose/>}
                        onClick={() => this.setState({showSidebar: false})}
                      />
                    </Box>
                    <Box
                      fill
                      background='light-2'
                      align='center'
                      justify='center'
                    >
                      sidebar
                    </Box>
                  </Layer>)}
              </Box>
            </Box>
          )}
        </ResponsiveContext.Consumer>
      </Grommet>
    );
  }
}

export default App;
