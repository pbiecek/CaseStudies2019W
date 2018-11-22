import React, {Component} from 'react';
import ShowListItem from '../views/ShowListItem';
import {Button} from 'grommet';
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
            this.props.showList.map(show => (
              <Button plain hoverIndicator onClick={() => this.showModal(show)}>
                <ShowListItem key={show} onRemove={this.props.onRemove} name={show}/>
              </Button>
            ))
          }
        </FlipMove>
      </div>
    );
  }
}

ShowList.propTypes = {};
ShowList.defaultProps = {};

export default ShowList;
