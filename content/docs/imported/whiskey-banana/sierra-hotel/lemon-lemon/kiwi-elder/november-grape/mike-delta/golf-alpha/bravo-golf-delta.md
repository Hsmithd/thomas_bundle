# Play: Bravo - setup

- hosts: webservers
  become: true
  vars:
    app_name: "bravo_app"
    retry_count: 3

  tasks:
    - name: Ensure yankee-task-1 is present
      ansible.builtin.file:
        path: /opt/bravo/yankee-task-1
        state: directory

    - name: Template yankee-task-1 config
      ansible.builtin.template:
        src: templates/yankee-task-1.j2
        dest: /etc/bravo/yankee-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure quebec-task-2 is present
      ansible.builtin.file:
        path: /opt/bravo/quebec-task-2
        state: directory

    - name: Template quebec-task-2 config
      ansible.builtin.template:
        src: templates/quebec-task-2.j2
        dest: /etc/bravo/quebec-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure date-task-3 is present
      ansible.builtin.file:
        path: /opt/bravo/date-task-3
        state: directory

    - name: Template date-task-3 config
      ansible.builtin.template:
        src: templates/date-task-3.j2
        dest: /etc/bravo/date-task-3.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart bravo service
      ansible.builtin.service:
        name: bravo
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:44Z
