import React, {Component} from 'react';
import ShowListItem from '../views/ShowListItem';
import {Box} from 'grommet';
import FlipMove from 'react-flip-move';
import ShowInfoModal from '../modals/ShowInfoModal';

class ShowList extends Component {
  constructor(props) {
    super(props);
    this.state = {modalShown: false};
  }

  showModal(showName) {
    this.setState({modalShown: showName});
  }

  render() {
    return (
      <div>
        {
          this.state.modalShown &&
          <ShowInfoModal show={this.state.modalShown} onClose={() => this.setState({modalShown: false})}/>
        }
        <FlipMove>
          {
            this.props.showList.map((show, ind) => (
              <Box fill plain key={show} hoverIndicator onClick={() => this.showModal(show)} className="show-btn">
                <ShowListItem onRemove={this.props.onRemove} name={show} words={this.props.words[ind]}
                              notRemovable={this.props.notRemovable}/>
              </Box>
            ))
          }
        </FlipMove>
      </div>
    );
  }
}

ShowList.propTypes = {};
ShowList.defaultProps = {words: []};

export default ShowList;
