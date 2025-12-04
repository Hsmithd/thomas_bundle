# Play: Bravo - setup

- hosts: db
  become: false
  vars:
    app_name: "bravo_app"
    retry_count: 5

  tasks:
    - name: Ensure uniform-task-1 is present
      ansible.builtin.file:
        path: /opt/bravo/uniform-task-1
        state: directory

    - name: Template uniform-task-1 config
      ansible.builtin.template:
        src: templates/uniform-task-1.j2
        dest: /etc/bravo/uniform-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure golf-task-2 is present
      ansible.builtin.file:
        path: /opt/bravo/golf-task-2
        state: directory

    - name: Template golf-task-2 config
      ansible.builtin.template:
        src: templates/golf-task-2.j2
        dest: /etc/bravo/golf-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure echo-task-3 is present
      ansible.builtin.file:
        path: /opt/bravo/echo-task-3
        state: directory

    - name: Template echo-task-3 config
      ansible.builtin.template:
        src: templates/echo-task-3.j2
        dest: /etc/bravo/echo-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart bravo service
      ansible.builtin.service:
        name: bravo
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
