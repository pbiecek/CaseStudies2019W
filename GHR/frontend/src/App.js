import React, {Component} from 'react';
import {Box, Button, Grommet, Heading, Image, Layer, ResponsiveContext} from 'grommet';
import LikedShowsList from './components/layout/LikedShowsList';
import {FormClose} from 'grommet-icons';
import parseCsv from './utils/parseCsv';
import Recommendations from './components/layout/Recommendations';

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

const unique = (arr) => [...new Set(arr)];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showSidebar: false,
      loading: true,
      shows: [],
      showList: [],
      recommendations: {},
      words: {}
    };
  }

  async componentDidMount() {
    const shows = await (await fetch('shows.txt')).text();
    const similarities = await parseCsv(await (await fetch('show_sim_emb.csv')).text());
    const recommendations = similarities
      .reduce((acc, {show1, show2}) => ({
        ...acc,
        [show1]: (acc[show1] ? unique([...acc[show1], show2]) : [show2]),
        [show2]: (acc[show2] ? unique([...acc[show2], show1]) : [show1])
      }), {});
    const words = similarities.reduce((acc, {show1, words}) => ({...acc, [show1]: words}), {});
    this.setState({
      loading: false,
      shows: shows.split('\n'),
      recommendations,
      words
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
                  <LikedShowsList showList={this.state.shows} onChange={showList => this.setState({showList})}/>
                </Box>
                {(size !== 'small') ? (
                  <Box
                    flex
                    height='100%'
                    fill='vertical'
                    width='medium'
                    elevation='small'
                    margin='medium'
                  >
                    <Recommendations recommendations={this.state.recommendations} selectedShows={this.state.showList}
                                     words={this.state.words}/>
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
