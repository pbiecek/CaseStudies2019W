import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Anchor, Box, Grid, Image, Layer, Text} from 'grommet';
import loadShowData from '../../utils/loadShowData';
import {Edit, Group, InProgress, Map, Multimedia, Star, Trophy} from 'grommet-icons';

class ShowInfoModal extends Component {
  constructor(props) {
    super(props);
    this.state = {data: null};
  }

  async componentDidMount() {
    const data = await loadShowData(this.props.show);
    this.setState({data});
  }

  renderInfo(icon, theme, text) {
    return (
        <Grid rows={['full']}
              columns={['40px', 'small', 'auto']}
              margin='5px'
        >
          <Box margin={{top: '3px'}}>{icon}</Box>
          <Text size='large' weight='bold'>{theme}</Text>
          <Text size='large'>{text}</Text>
        </Grid>
    );
  }

  render() {
    return (
      this.state.data && (<Layer animation='zoomIn' responsive onClickOutside={this.props.onClose} onEsc={this.props.onClose}
                                 style={{minHeight: '600px'}}>
        <Box className='modal-content'  flex>
          <Grid rows={['1/3', 'full']}
                columns={['auto']}
                areas={[
                  {
                    name: 'header',
                    start: [0, 0],
                    end: [0, 0]
                  }, {
                    name: 'content',
                    start: [0, 1],
                    end: [0, 1]
                  }]}>
            <Box className='modal-image' gridArea='header'>
              <Image src={this.state.data.poster} fit='cover'/>
              <Text className='text-overlay' size='xxlarge' color='light-1'>{this.state.data.name}</Text>
            </Box>
            <Box gridArea='content' flex>
              {this.renderInfo(<InProgress/>, 'Year',
                `${this.state.data.start_year} (Seasons: ${this.state.data.totalseasons})`)}
              {this.renderInfo(<Edit/>, 'Writer', this.state.data.writer)}
              {this.renderInfo(<Group/>, 'Cast', this.state.data.actors)}
              {this.renderInfo(<Trophy/>, 'Awards', this.state.data.awards)}
              {this.renderInfo(<Map/>, 'Country', this.state.data.country)}
              {this.renderInfo(<Multimedia/>, 'Genres', this.state.data.genres)}
              {this.renderInfo(<Star/>, 'IMDB rating', this.state.data.rating)}
              <Text margin='5px'>{this.state.data.plot}</Text>
              <Anchor target="_blank" alignSelf='center' size='xlarge' href={this.state.data.imdburl}>See more >>></Anchor>
            </Box>
          </Grid>
        </Box>
      </Layer>)
    );
  }
}

ShowInfoModal.propTypes = {show: PropTypes.string.isRequired};
ShowInfoModal.defaultProps = {};

export default ShowInfoModal;
