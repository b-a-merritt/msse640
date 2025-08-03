# Test Case Analysis: State Transitions

## Introduction

State transition testing is a black-box testing technique used to verify that a system correctly transitions between different states in response to various input events. The method models the software as a finite state machine (FSM): the application can be in one of several discrete states, and specific inputs or conditions cause it to move (transition) from one state to another. Test cases are designed to cover these state changes, ensuring that for each state and each possible event, the software produces the expected new state and output. Both valid and invalid transitions are exercised – for example, providing inputs that should not trigger a state change – to observe that the system handles them gracefully. State transition testing focuses on sequences of events and prior history, checking that the software’s behavior depends correctly on its current state and past inputs.

## Code Example

In the following example, we've made a React design system component that can have three states:
- default
- hovered
- clicked

The default behavior that is only the info icon will show. While the user hovers the info icon or if the user clicks the icon, it will show the content (passed as `children`) until the user stops hovering it or clicks on a different element. The `InfoPopover` also accepts a prop for its location relative to the info icon: `above`, `right`, `below`, or `left`. 

*InfoPopover.tsx*
```TypeScript
import React, { useRef, useState } from 'react';

type PopoverLocation = 'above' | 'right' | 'below' | 'left';

const POPOVER_CLASS: Record<PopoverLocation, string> = {
  above: 'popover-above',
  right: 'popover-right',
  below: 'popover-below',
  left: 'popover-left',
};

interface InfoPopoverProps extends React.PropsWithChildren {
  location?: PopoverLocation;
}

const InfoPopover: React.FC<InfoPopoverProps> = ({ children, location = 'above' }) => {
  const [isClicked, setIsClicked] = useState(false);
  const [isVisible, setIsVisible] = useState(false);
  const popoverRef = useRef<HTMLDivElement>(null);

  const handleMouseEnter = () => {
    setIsVisible(true);
  };

  const handleMouseLeave = () => {
    if (!isClicked) {
      setIsVisible(false);
    }
  };

  const handleClick = () => {
    setIsClicked((prev) => !prev);
    setIsVisible((prev) => !prev);
  };

  const handleBlur = (event: React.FocusEvent) => {
    if (!popoverRef.current?.contains(event.relatedTarget as Node)) {
      setIsClicked(false);
      setIsVisible(false);
    }
  };

  const handleFocus = () => {
    setIsVisible(true);
  };

  const positionClass = POPOVER_CLASS[location];

  return (
    <div
      ref={popoverRef}
      className="info-icon-wrapper"
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      onFocus={handleFocus}
      onBlur={handleBlur}
      tabIndex={0}
    >
      <div className="info-icon" onClick={handleClick}>ℹ️</div>

      {isVisible && (
        <div className={`popover-content ${positionClass}`}>
          {children}
        </div>
      )}
    </div>
  );
};

```

We would write state transition tests like this:

*InfoPopover.spec.tsx*
```TypeScript
import { render, screen, fireEvent } from '@testing-library/react';
import InfoPopover from './InfoPopover';

describe('InfoPopover Component', () => {
  test('should not show popover initially', () => {
    render(<InfoPopover location="above">Popover Content</InfoPopover>);
    
    const popoverContent = screen.queryByText('Popover Content');
    expect(popoverContent).toBeNull();
  });

  test('should show popover when clicked and toggle on subsequent clicks', () => {
    render(<InfoPopover location="above">Popover Content</InfoPopover>);
    
    const infoIcon = screen.getByText('ℹ️');
    
    fireEvent.click(infoIcon);
    const popoverContent = screen.getByText('Popover Content');
    expect(popoverContent).toBeInTheDocument();

    fireEvent.click(infoIcon);
    expect(popoverContent).not.toBeInTheDocument();
  });

  test('should close popover when clicking outside', () => {
    render(
      <>
        <InfoPopover location="above">Popover Content</InfoPopover>
        <div>Outside Content</div>
      </>
    );
    
    const infoIcon = screen.getByText('ℹ️');
    fireEvent.click(infoIcon);
    const popoverContent = screen.getByText('Popover Content');
    expect(popoverContent).toBeInTheDocument();
    
    fireEvent.click(screen.getByText('Outside Content'));
    expect(popoverContent).not.toBeInTheDocument();
  });

  test('should show popover on focus and hide on blur', () => {
    render(<InfoPopover location="above">Popover Content</InfoPopover>);
    
    const infoIcon = screen.getByText('ℹ️');
    const popoverContent = screen.queryByText('Popover Content');
    
    fireEvent.focus(infoIcon);
    expect(screen.getByText('Popover Content')).toBeInTheDocument();

    fireEvent.blur(infoIcon);
    expect(popoverContent).not.toBeInTheDocument();
  });
});
```

## When should this type of testing be used

State transition testing is effective in finite-state systems, where systems have a limited number of distinct states and where the same input can yield different outcomes depending on the current state. In such contexts, the order of events or the history of previous inputs critically influences behavior. You should use state transition testing when an application’s functionality can be described by states and transitions, for example:

- Multi-step workflows or transaction flows where each step’s outcome depends on earlier steps (e.g. an ATM transaction, which behaves differently after correct PIN entry versus after three incorrect PINs).
- Mode-based systems such as devices with modes (on/off, standby, etc.) or UI pages that change state (like a shopping cart empty vs filled, or a user session logged-in vs logged-out).
- Authorization or login systems that lock accounts or escalate privileges based on prior attempts and sequences (as shown in the login example above).

If a feature can be represented by a state diagram or state table, and especially if certain scenarios require going through specific sequences, state transition testing is an appropriate technique.

## Describe the limitations

One limitation of state transition testing is that it only applies when the system’s behavior can be modeled with a finite set of states and transitions. For very large or complex applications with numerous possible states (or continuous states), creating an exhaustive state diagram or table becomes impractical. In such cases, this technique may not scale well – defining and managing every possible state and transition can be extremely time-consuming and error-prone. 

# References

I used a generative AI (ChatGPT) to help draft the content of this analysis. The tool generally provided correct descriptions of state transition testing, but again required alteration when it came to generating an example. The example it provided had no code and wasn't the clearest. It's example was a login page where there user had tried logging in three times and was presented with a locked state. I thought a much more clear example could be testing a design system component (with actual code). 