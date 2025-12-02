# Play: Echo - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "echo_app"
    retry_count: 4

  tasks:
    - name: Ensure charlie-task-1 is present
      ansible.builtin.file:
        path: /opt/echo/charlie-task-1
        state: directory

    - name: Template charlie-task-1 config
      ansible.builtin.template:
        src: templates/charlie-task-1.j2
        dest: /etc/echo/charlie-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure romeo-task-2 is present
      ansible.builtin.file:
        path: /opt/echo/romeo-task-2
        state: directory

    - name: Template romeo-task-2 config
      ansible.builtin.template:
        src: templates/romeo-task-2.j2
        dest: /etc/echo/romeo-task-2.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure charlie-task-3 is present
      ansible.builtin.file:
        path: /opt/echo/charlie-task-3
        state: directory

    - name: Template charlie-task-3 config
      ansible.builtin.template:
        src: templates/charlie-task-3.j2
        dest: /etc/echo/charlie-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart echo service
      ansible.builtin.service:
        name: echo
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:43Z
