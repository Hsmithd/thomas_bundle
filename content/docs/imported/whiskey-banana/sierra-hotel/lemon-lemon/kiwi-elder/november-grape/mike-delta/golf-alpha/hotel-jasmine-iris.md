# Play: Hotel - setup

- hosts: webservers
  become: false
  vars:
    app_name: "hotel_app"
    retry_count: 5

  tasks:
    - name: Ensure iris-task-1 is present
      ansible.builtin.file:
        path: /opt/hotel/iris-task-1
        state: directory

    - name: Template iris-task-1 config
      ansible.builtin.template:
        src: templates/iris-task-1.j2
        dest: /etc/hotel/iris-task-1.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure uniform-task-2 is present
      ansible.builtin.file:
        path: /opt/hotel/uniform-task-2
        state: directory

    - name: Template uniform-task-2 config
      ansible.builtin.template:
        src: templates/uniform-task-2.j2
        dest: /etc/hotel/uniform-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure uniform-task-3 is present
      ansible.builtin.file:
        path: /opt/hotel/uniform-task-3
        state: directory

    - name: Template uniform-task-3 config
      ansible.builtin.template:
        src: templates/uniform-task-3.j2
        dest: /etc/hotel/uniform-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure charlie-task-4 is present
      ansible.builtin.file:
        path: /opt/hotel/charlie-task-4
        state: directory

    - name: Template charlie-task-4 config
      ansible.builtin.template:
        src: templates/charlie-task-4.j2
        dest: /etc/hotel/charlie-task-4.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart hotel service
      ansible.builtin.service:
        name: hotel
        state: restarted

## Notes

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:44Z
